import random
import math

# function func(x) {
#   let T = 8760;
#   return ((x[0] > T && x[1] > T) || (x[2] > T && x[3] > T)) && (x[4] > T) && (x[5] > T) && (
#     x[6] > T || x[7] > T || x[8] > T) && (x[9] > T || x[10] > T) && (x[11] > T || x[12] > T)
# }

def func(x):
    T = 8760;
    return 
    ((((x[0] > T) & (x[1] > T)) | ((x[2] > T) & (x[3] > T))) & 
    (x[4] > T) & (x[5] > T) & 
    ( ((x[6] > T) & (x[7] > T)) | ((x[8] > T) & (x[9] > T)) | ((x[10] > T) & (x[11] > T)) )); 

m = 3




def work(L):
    N = 33012
    m = 3
    lambdas = [40 * 10 ** -6, 10 * 10 ** -6, 80 * 10 ** -6, ]
    n = [4,2,6]
    d = 0

    for k in range(0,N):
        x = []

        for i in range(0,m):
            t = []
            for j in range(0,n[i]):
                a =random.random()
                t.append(-math.log(a) / lambdas[i])

            for j in range(0, L[i]):
                l = t.index(min(t))
                t[l] = t[l] - math.log(random.random()/lambdas[i])

            for j in range(0,n[i]):
                x.append(t[j])
        
        if not func(x):
            d = d + 1

    return 1 - d / N;


# ((x1 ∧ x2)∨(x3 ∧ x4)) ∧ x5 ∧ x6 ∧ ((x7 ∧ x8)∨(x9 ∧ x10)∨(x11 ∧ x12))

# function work(L) {
#   let N = 33012;
#   let m = 4;
#   let lambdaF = [40 * (10 ** -6), 10 * (10 ** -6), 80 * (10 ** -6), 30 * (10 ** -6)];

#   let n = [4, 2, 3, 4];
#   let d = 0;
#   for (let k = 0; k < N; k++) {
#     let x = [];
#     for (let i = 0; i < m; i++) {
#       let t = [];
#       for (let j = 0; j < n[i]; j++) {
#         let alpha = Math.random();
#         t.push(-Math.log(alpha) / lambdaF[i]);
#       }


#       for (let j = 0; j < L[i]; j++) {
#         let l = t.indexOf(Math.min(...t));
#         t[l] = t[l] - (Math.log(Math.random()) / lambdaF[i]);
#       }

#       for (let j = 0; j < n[i]; j++) {
#         x.push(t[j]);
#       }
#     }
#     if (!func(x)) {
#       d++;
#     }
#   }
#   return 1 - d / N
# }

P0 = 0.999
L = [0,0,0]

wt = 3

for i in range (0,wt):
    L[0] = i

    for j in range(0,wt):
        L[1] = j
        
        for k in range (0,wt):
            
            L[2] = k
            P = work(L)

            if (P > P0):
                print("LOOK ABOVE")
                print("P = ", P, "L = ", " ", sum(L))



# let p0 = 0.995;
# let L = [0, 0, 0, 0];
# for (let i = 0; i < 5; i++) {
#   L[0] = i;
#   for (let j = 0; j < 5; j++) {
#     L[1] = j;
#     for (let s = 0; s < 5; s++) {
#       L[2] = s
#       for (let k = 0; k < 5; k++) {
#         L[3] = k
#         P = work(L)
#         if (P > p0)
#           // console.log("LOOK ABOVE");
#           console.log("P = ", P, " L = ", L, "   ", L.reduce((acc, val) => acc + val))
#       }
#     }
#   }
# }