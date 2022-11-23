This repository provides a solution to the problem stated in the following link :
https://www.chegg.com/homework-help/questions-and-answers/n-blocks-numbered-0-n-1-arranged-row-couple-frogs-sitting-together-one-block-terrible-quar-q79338186

There are two versions of the code :
* V1 is the naive approach considering all the possibilities and doing the computations all over again at each iteration. Complexity O(len(A)**2).
* V2 makes use of pre-fix and post-fix sums to reduce the complexity of the computation. Complexity O(len(A)).
