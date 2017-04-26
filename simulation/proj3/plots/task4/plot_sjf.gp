set terminal postscript eps enhanced color 15 "Helvetica"
set output "sjf.eps"
set title "First Come First Serve"

load '~/.config/grid.cfg'
load '~/.config/greys.pal'
load '~/.config/xyborder.cfg'

set xrange [0:101]
set logscale y 2
set ylabel "Slowdown"
set xlabel "Bins"
set size ratio 1
set key outside vert right top noreverse noenhanced autotitle nobox
plot "./MM1/SJF" using 1:2 w lines ls 16 lw 3 title "M/M/1", \
     "./MG1/SJF" using 1:2 w lines ls 15 lw 3 title "M/G/1"
