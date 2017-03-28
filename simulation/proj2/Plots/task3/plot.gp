set terminal postscript eps enhanced color 15 "Helvetica"
set output "overall_wait_time.eps"
unset key
set yrange [4:4.5]
set size ratio 1
set boxwidth 0.9 absolute
set style fill solid 1.00 border lt 0
set key inside right top vertical Right noreverse noenhanced autotitle nobox
set title "Overall Average Wait Times"
set xlabel "{/Symbol r}"
set ylabel "Wait Times"
plot "wait_times.dat" using 1:2:3:4 with errorbars notitle
