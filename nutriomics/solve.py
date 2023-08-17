from functools import partial
import scipy
import scipy.optimize
from tqdm import tqdm

def convert_problem_into_lp(u, v_low, v_high, nim, sparsity_penalty, constraint_violation_penalty):
    # min violations of v_low <= nim * x + u <= v_high, x should be sparse
    n, m = nim.shape
    assert u.shape[0] == v_low.shape[0] == v_high.shape[0] == n
    constraint_coef = []
    bias_v = []
    for i in range(n):
        # nim * x - 1 * y <= v_high - u
        constraint_coef.append(nim[i].tolist() + [-1 if j == i else 0 for j in range(2 * n)])
        bias_v.append(v_high[i] - u[i])
    for i in range(n):
        # -nim * x - 1 * y <= -v_low + u
        constraint_coef.append((-nim[i]).tolist() + [-1 if j - n == i else 0 for j in range(2 * n)])
        bias_v.append(-v_low[i] + u[i])
    c = []
    for i in range(m):
        c.append(sparsity_penalty)
    for i in range(2 * n):
        c.append(constraint_violation_penalty)
    return np.array(constraint_coef), np.array(bias_v), np.array(c)

# nim_np = nim.to_numpy()

# A, b, c = convert_problem_into_lp(deviant_taxonomy[:, 0], vlow, vhigh, nim_np, 0., 0.0)
# print(A.shape, b.shape, c.shape)
# import scipy.optimize
# r = scipy.optimize.linprog(c, A_ub=A, b_ub=b, A_eq=None, b_eq=None, bounds=None, method='highs', callback=None, options=None, x0=None)

# print(r.x[: 80].nonzero())
# print(r.success)
# print(violations(deviant_taxonomy[:, 0]))
# print(violations((nim_np @ r.x[: 80][:, np.newaxis]).squeeze(1) + deviant_taxonomy[:, 0]))


nim_np = nim.to_numpy()
nvars = nim_np.shape[1]

def grid_search(k_sparse, sparsity_low, sparsity_high, sparsity_delta, violation_low, violation_high, violation_delta, lp_fn, eval_fn):
    best_answer = 1e9
    sparsity_chunks = int((sparsity_high - sparsity_low) / sparsity_delta + 0.5)
    violation_chunks = int((violation_high - violation_low) / violation_delta + 0.5)
    for sparsity_i in range(sparsity_chunks):
        sparsity_p = sparsity_low + sparsity_i * sparsity_delta
        for violation_i in range(violation_chunks):
            violation_p = violation_low + violation_i * violation_delta
            r = lp_fn(sparsity_penalty=sparsity_p, constraint_violation_penalty=violation_p)
            if r.success:
                non_zero_elements = len(r.x[: nvars].nonzero()[0])
                if non_zero_elements <= k_sparse:
                    best_answer = min(best_answer, eval_fn(r.x[: nvars]))
    return best_answer

def binary_search(k_sparse, sparsity_low, sparsity_high, sparsity_delta, violation_low, violation_high, violation_delta, lp_fn, eval_fn):
    best_answer = 1e9
    # sparsity_p higher -> valid x
    # violation_p higher -> better sol
    # highest violation such that sparsity is satisfied
    while violation_low < violation_high - violation_delta:
        violation_p = (violation_low + violation_high) / 2
        s_low = sparsity_low
        s_high = sparsity_high
        found = False
        while s_low < s_high - sparsity_delta:
            sparsity_p = (s_low + s_high) / 2
            r = lp_fn(sparsity_penalty=sparsity_p, constraint_violation_penalty=violation_p)
            if r.success and len(r.x[: nvars].nonzero()[0]) <= k_sparse:
                best_answer = min(best_answer, eval_fn(r.x[: nvars]))
                s_high = sparsity_p
                found = True
            else:
                s_low = sparsity_p
        if found:
            violation_low = violation_p
        else:
            violation_high = violation_p
    return best_answer

def solve_problem_with_lp(u, v_low, v_high, nim, sparsity_penalty, constraint_violation_penalty):
    A, b, c = convert_problem_into_lp(u, v_low, v_high, nim, sparsity_penalty, constraint_violation_penalty)
    return scipy.optimize.linprog(c, A_ub=A, b_ub=b, method='highs')

k_sparse = 10
violations_before = []
violations_after = []
for deviant_sample in tqdm(deviant_taxonomy.T):
    lp_fn = partial(solve_problem_with_lp, u=deviant_sample, v_low=vlow, v_high=vhigh, nim=nim_np)
    def eval_fn(x):
        return violations((nim_np @ x[:, np.newaxis]).squeeze(1) + deviant_sample)[0]
    best_answer = grid_search(k_sparse, 0, 1, 0.2, 0, 1, 0.2, lp_fn, eval_fn)
#     print("violations", violations(deviant_sample)[0], "->", best_answer)
    violations_before.append(violations(deviant_sample)[0])
    violations_after.append(best_answer)
print(np.mean(violations_before), np.mean(violations_after))