program SUM10FOR;
var n, sum, i;
begin
    n := 10;
    sum := 0;
    for i := 1 to n do
        sum := sum + i;
    write(sum)
end.
