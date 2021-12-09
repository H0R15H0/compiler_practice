program SUM10WHILE;
var n, sum;
begin
    n := 10;
    sum := 0;
    while n > 0 do
    begin
        sum := sum + n;
        n := n - 1
    end;
    write(sum)
end.
