program PL2A;
var n;
function fact(n);
begin
    if n <= 0 then
        fact := 1
    else
        fact := fact(n - 1) * n
end;
begin
    read(n);
    write(fact(n))
end.
