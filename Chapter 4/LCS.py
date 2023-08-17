# Adam Klie
# CSE182 Discussion 3 LCS code
# 04/14/2021

# Import needed packages, all these are ok for the course (but if you're not sure about one, ask!)
import argparse
import numpy as np
import matplotlib.pyplot as plt
import random
import string

# Function to compute LCS between two strings
def LCS(S, T):
    L = np.zeros(shape=(len(S)+1, len(T)+1))
    for i in range(1, len(S)+1):
        for j in range(1, len(T)+1):
            tmp = -np.inf
            if S[i-1] == T[j-1]:
                tmp = L[i-1, j-1]+1
            L[i, j] = max(L[i-1, j], L[i, j-1], tmp)
    return int(L[len(S), len(T)])


# Function to generate a random uppercase string of an input a length
def random_string(s_len):
    # Implement it yourself :)

# Function to compute LCSs for an input string an n random sequences of the same length
def random_LCS(st, num_seq=100, seq_len=50):
    lcs_lens = [LCS(st, random_string(len(st))) for i in range(num_seq)]
    return lcs_lens


# What will actually be run when you call `LCS.py` (can also use a main function here)

# Parse the input arguments
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--string1', type=str, help='first string', required=True)
parser.add_argument('-t', '--string2', type=str, help='second string', required=False)
parser.add_argument('-p', '--plot_hist', type=bool, default=False, help='True/False, whether to plot empirical LCS histogram')
parser.add_argument('-n', '--num_seqs', type=int, default=100, help='Only used if -p set to true, number of random strings')
parser.add_argument('-f', '--save_file', type=str, default='discussion_demo_out.png', help='Filename to save the histogram')
args = parser.parse_args()

# Get the strings, the 1st one should be provided in input, but the second may need to be generated
s = args.string1
if args.string2 == None:
    t = random_string(len(s))
else:
    t = args.string2

# Calculate the LCS and print for these strings
print("LCS between \n{}\n{}\nhas length: {}".format(s, t, LCS(s, t)))

# If the histogram argument is True, plot an empirical histogram of LCSs for random sequence to seq of interest
if args.plot_hist:
    plot_lens = random_LCS(s, num_seq=args.num_seqs)
    print(plot_lens)
    plt.hist(plot_lens)
    plt.xlabel('LCS Length')
    plt.ylabel('Frequency')
    plt.savefig(args.save_file)
    plt.show()
