#!/bin/zsh
#SBATCH --ntasks=64
#SBATCH --job-name=vectorize
#SBATCH --cpus-per-task=12

N=64

rm -rf vectors
mkdir vectors
#rm -rf input_data
#mkdir input_data
#cd input_data
#split -d --additional-suffix=.txt -l "$(( $(wc -l ../articles.txt | cut -d ' ' -f 1) /$N + 1))" ../articles.txt article_
#cd ..
#ls

for j in $(seq 0 $((N-1))); do
    srun --cpus-per-task=12 python search2.py < "input_data/article_$(printf %02d $j).txt" > vectors/$j.txt &
done
wait
