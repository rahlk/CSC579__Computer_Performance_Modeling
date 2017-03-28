set terminal postscript eps enhanced color 15 "Helvetica"
set output "Disk_1_wait_time.eps"
unset key
set autoscale
set size ratio 1
set boxwidth 0.9 absolute
set style fill solid 1.00 border lt 0
set key inside right top vertical Right noreverse noenhanced autotitle nobox
set title "Disk 1 Wait Time"
set xlabel "{/Symbol r}"
set ylabel "Wait Times"
plot "wait_times.dat" using 1:8:9:10 with errorbars
