program PL0B;
var n, x;
procedure prime;
var n;
begin
    n := x div 2;
    while x <> (x div n) * n do
        n := n - 1;
    if n = 1 then
        write(x)
end;
begin
    read(n);
    while 1 < n do
    begin
        x := n;
        prime;
        n := n - 1
    end
end.
