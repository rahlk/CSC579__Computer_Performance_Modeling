set terminal postscript eps enhanced color 20 "Helvetica"
set output "sjf.eps"
set title "Shortest Job First"

load '~/.config/grid.cfg'
load '~/.config/greys.pal'
load '~/.config/xyborder.cfg'

set xrange [0:10]
set ylabel "System Time"
set xlabel "Rho"
set size ratio 1
set key outside vert right top noreverse noenhanced autotitle nobox
plot "./MM3/SJF" using 1:3:4:5:xticlabels(2) with yerrorbars ls 16 lw 3 title "M/M/3", \
     "./MM3/SJF" using 1:3 w lines ls 16 lw 3 title "", \
     "./MG3/SJF" using 1:3:4:5:xticlabels(2) with errorbars ls 15 lw 3 title "M/G/3", \
     "./MG3/SJF" using 1:3 w lines ls 15 lw 3 title "", \
