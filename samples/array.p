program ARRAY;
var a[1..10], i, s;
begin
    i := 1;
    while i <= 10 do
    begin
        a[i] := i;
        i := i + 1
    end;
    i := 1;
    while i <= 10 do
    begin
        s := a[i] + s;
        i := i + 1
    end
end.
