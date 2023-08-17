#!/usr/bin/env python
# coding: utf-8

# In[1]:


PAM250 = {'A': {'A': 2, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N': 0,
                'P': 1, 'Q': 0, 'R': -2, 'S': 1, 'T': 1, 'V': 0, 'W': -6, 'Y': -3},
          'C': {'A': -2, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5,
                'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S': 0, 'T': -2, 'V': -2, 'W': -8, 'Y': 0},
          'D': {'A': 0, 'C': -5, 'D': 4, 'E': 3, 'F': -6, 'G': 1, 'H': 1, 'I': -2, 'K': 0, 'L': -4, 'M': -3, 'N': 2,
                'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
          'E': {'A': 0, 'C': -5, 'D': 3, 'E': 4, 'F': -5, 'G': 0, 'H': 1, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1,
                'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
          'F': {'A': -3, 'C': -4, 'D': -6, 'E': -5, 'F': 9, 'G': -5, 'H': -2, 'I': 1, 'K': -5, 'L': 2, 'M': 0, 'N': -3,
                'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W': 0, 'Y': 7},
          'G': {'A': 1, 'C': -3, 'D': 1, 'E': 0, 'F': -5, 'G': 5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N': 0,
                'P': 0, 'Q': -1, 'R': -3, 'S': 1, 'T': 0, 'V': -1, 'W': -7, 'Y': -5},
          'H': {'A': -1, 'C': -3, 'D': 1, 'E': 1, 'F': -2, 'G': -2, 'H': 6, 'I': -2, 'K': 0, 'L': -2, 'M': -2, 'N': 2,
                'P': 0, 'Q': 3, 'R': 2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y': 0},
          'I': {'A': -1, 'C': -2, 'D': -2, 'E': -2, 'F': 1, 'G': -3, 'H': -2, 'I': 5, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
                'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -5, 'Y': -1},
          'K': {'A': -1, 'C': -5, 'D': 0, 'E': 0, 'F': -5, 'G': -2, 'H': 0, 'I': -2, 'K': 5, 'L': -3, 'M': 0, 'N': 1,
                'P': -1, 'Q': 1, 'R': 3, 'S': 0, 'T': 0, 'V': -2, 'W': -3, 'Y': -4},
          'L': {'A': -2, 'C': -6, 'D': -4, 'E': -3, 'F': 2, 'G': -4, 'H': -2, 'I': 2, 'K': -3, 'L': 6, 'M': 4, 'N': -3,
                'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': 2, 'W': -2, 'Y': -1},
          'M': {'A': -1, 'C': -5, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 2, 'K': 0, 'L': 4, 'M': 6, 'N': -2,
                'P': -2, 'Q': -1, 'R': 0, 'S': -2, 'T': -1, 'V': 2, 'W': -4, 'Y': -2},
          'N': {'A': 0, 'C': -4, 'D': 2, 'E': 1, 'F': -3, 'G': 0, 'H': 2, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2,
                'P': 0, 'Q': 1, 'R': 0, 'S': 1, 'T': 0, 'V': -2, 'W': -4, 'Y': -2},
          'P': {'A': 1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G': 0, 'H': 0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N': 0,
                'P': 6, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -1, 'W': -6, 'Y': -5},
          'Q': {'A': 0, 'C': -5, 'D': 2, 'E': 2, 'F': -5, 'G': -1, 'H': 3, 'I': -2, 'K': 1, 'L': -2, 'M': -1, 'N': 1,
                'P': 0, 'Q': 4, 'R': 1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
          'R': {'A': -2, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H': 2, 'I': -2, 'K': 3, 'L': -3, 'M': 0, 'N': 0,
                'P': 0, 'Q': 1, 'R': 6, 'S': 0, 'T': -1, 'V': -2, 'W': 2, 'Y': -4},
          'S': {'A': 1, 'C': 0, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': 0, 'L': -3, 'M': -2, 'N': 1,
                'P': 1, 'Q': -1, 'R': 0, 'S': 2, 'T': 1, 'V': -1, 'W': -2, 'Y': -3},
          'T': {'A': 1, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 0, 'H': -1, 'I': 0, 'K': 0, 'L': -2, 'M': -1, 'N': 0,
                'P': 0, 'Q': -1, 'R': -1, 'S': 1, 'T': 3, 'V': 0, 'W': -5, 'Y': -3},
          'V': {'A': 0, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I': 4, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
                'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -6, 'Y': -2},
          'W': {'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4,
                'N': -4, 'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y': 0},
          'Y': {'A': -3, 'C': 0, 'D': -4, 'E': -4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2,
                'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'Y': 10}}


# In[34]:


def matrix_helper(x, y):
    return [[0]*y for i in range(x)]
def LocalAlignment(seq1, seq2, indel_penalty = 5):
    n = len(seq1)
    m = len(seq2)
    score = matrix_helper(n+1, m+1)
    backtrack = matrix_helper(n+1, m+1)
    best = 0
    optimal = (0,0)
    for i in range(1,n+1):
        for j in range(1,m+1):
            down = score[i-1][j] - indel_penalty
            right = score[i][j-1] - indel_penalty
            diag = score[i-1][j-1] + PAM250[seq1[i-1]][seq2[j-1]]
            score[i][j] = max(down,
                              right,
                              diag,
                              0)
            if score[i][j] >= best:
                best = score[i][j]
                optimal = (i,j)
            #down
            if score[i][j] == down:
                if score[i-1][j] < 0 and score[i][j-1] < 0 and score[i-1][j-1] < 0:
                    backtrack[i][j] = 0 
                else:
                    backtrack[i][j] = 1
            #right
            elif score[i][j] == right:
                if score[i-1][j] < 0 and score[i][j-1] < 0 and score[i-1][j-1] < 0:
                    backtrack[i][j] = 0 
                else:
                    backtrack[i][j] = 2
            #diagonal
            elif score[i][j] == diag:
                backtrack[i][j] = 3
    x = optimal[0]
    y = optimal[1]
    a1 = ''
    a2 = ''
    working = backtrack[x][y]
    while(working > 0):
        if working == 3:
            x -= 1
            y -= 1
            a1 = seq1[x] + a1
            a2 = seq2[y] + a2
        elif working == 2:
            y -= 1
            a1 = '-' + a1
            a2 = seq2[y] + a2
        elif working == 1:
            x -= 1
            a1 = seq1[x] + a1
            a2 = '-' + a2
        working = backtrack[x][y]
    print ("Alignment sequence 1: " + a1)
    print ("Alignment sequence 2: " + a2)
    return best, a1, a2


# In[31]:


seq1 = "DYAGHGDPRQPKQDL"
seq2 = "VFQDIGDYMQWDNVK"

LocalAlignment(seq1, seq2)


# In[38]:


LocalAlignment(seq1, seq2)


# In[37]:


seq1 = "HWLKIDWSTPRLWWQKVGINPERCIVKCGCSCFVYQSPPDGGPNYEHWECVWDKKVVTDQGIWISLFEHKKFLAMLRLIAEHQGSPICMGGQQKTIVNLHNAHWVATTEDSQMPRSQYMDGCHMQSTSSTWTVKPMVRTRFRFGFWKAGPLHKHVDPHWKHMQVRFGIVGIGDYQRGVHAFMWKPDTEQTIHGGWDVGFAHCKIWYIKQWYCWCSLCARDNWSHCIDCLRPKENTMGWPFDGAIAGNGLFWYCSPGIKPTVVEFRDCNHSSIERIVTTVHHLPGLYMTYLAMTAPAKPFSIIWGSNNHDAYTMHLMEKYQNISQMRPEIWQKYMEHHPNRSPQKYKRHFYEFWEMASQSEVYGYRGPNMYADVALMAKISHETNDDNMFSPHDLHFACPWETIDPAYGLFQPYKRYKFGKDTADDSDQLTPSPLMLICENAWKVMYIACTGCCCHHCYIHKTCYCISNAMAVPFCTRKMRVKNYNCMWDKLQCSGFQSYHETLIDPVFIVAQNYSWSPRWDFNIHHTDPVLEKLAWAHKPTVGATVRAQRNDYMKRVVCHQIGPAWHISYTHYADRPTFREGEDERPATQIVAVWWEHVTNWHSSQLITDYVRAYDWYESFEMPWQYHHRKKSNSCIWWEPNAPRQWTIRVKPVEAPLGSVRECCGFWIGSGNDYRPYTKYASGHCAEPTTNMMYMKNKHQFLTYMFKLIPYQSNCHIIYITNGGIKHCLYKWVCYNRWYNIMNSEVWMLLKLTVQFSLGNFLWEWKEQCNNHQFYPRTKYPWQEFGDNMTLCARMTSQHNVHKDWFVHYHVPIRPKHDNLHWLLEYLNCKYPIIWLNDMCLFWRYQIERENLMMFPPCYGQMQYLCIYWFKAGRPLRYRRLRQIGCHLTNLQLQGQDKH"
seq2 = "LMEHFKAIYLNSDAQGESQYTTPPNASICDTYPEHQAGSSDHKFHKRGSLLMRHHGTGPKCKCRYRRQCTGHFGCQPTMSYHISWMLIQKEMEYWPYWIISIRWGHGYLCWVVAGNLDIISGFAGIHMWHLYWETGQRKSNGITLWWVKALWVYGFITEDMVTYQTYTSGWIHNLTTGMKPDMGIFENFSPICDEWEKILMRWSNPAHPNTGIPHCLEECPSLAPPIKSEYMVCAWYCRECIFHMHRKWAFCPSWKPIWSICLIWMCVALVCAMCRCPYLLMTAPAKPESIIWGSNLSRFVQVDCMEVKYQHQYASFNISQMRVSGSESPQKYKRHFTLKCEFTPKKETEMASQSEVYGTRGPNMYADVRYPMAKISHRKLWPIKNDDNMFSSHDLHFACPWIENTTDPAYGLFQPYKRSKFGKDTVGDDSCENAWKVMYIARPSERPYVWMQCPRQNYVHYTCYQYVPFCTRKMRVKNYWDQLIDPVFIVGWNCPGGHCSPFNWSVMCYRWDFNIHHRDPVAEAAGDIQQCWKPTVFRCGATVRAQRPDYMQPIFHPIRVCCHQIGPANHISATHYADRPTFSTNPKSWHSSQLITDYWHFIKFIEHSVAHYESFEMQYHHNKRDWEPNIEMSLLKIVYKEWHHVWDAFFEKIGTETRLRQCYCFRLSPQKKFTLQCALIPTTQRKYPDKGDFKMPCGDVTATYDHVDSAVFTCKEWEMSFIIQFQNRSCVCSRHLCSNRLFCVAAKLETINYQSPFMRWKQPHYQPTKLSGFDNSIVCSHCPHEDTECMDNVCAKLAAIDLQRLDTLVQELWILCATQSVDIADFNLYTKWQDDQRADFYSVGPSMMMLDQENGICNAYITLITMWLIGTCGPWKNDHMTPRTCSEMPLFDYVERG"


# In[ ]:




