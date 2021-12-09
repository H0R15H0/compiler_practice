program ZERO;
var x, y;
begin
    x := 0;
    if x <> 0 then
    begin
        if x < 0 then
            y := -2
        else
            y := 2;
        x := 1
    end
    else
        y := 0;

    write(y)
end.
