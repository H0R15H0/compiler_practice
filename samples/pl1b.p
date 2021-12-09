program PL1B;
var m, n, result;
procedure power(m,n);
var i;
begin
    result := 1;
    for i := 1 to n do
        result := result * m
end;
begin
    read(m);
    read(n);
    power(m,n);
    write(result)
end.
