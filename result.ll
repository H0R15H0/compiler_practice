@x = common global i32 0, align 4
@y = common global i32 0, align 4

define i32 @main() {
    store i32 0, i32* @x, align 4
    %1 = load i32, i32* @x, align 4
    %2 = icmp ne i32 %1, 0
    br i1 %2, label %L1, label %L2
    L1:
    %3 = load i32, i32* @x, align 4
    %4 = icmp slt i32 %3, 0
    br i1 %4, label %L4, label %L5
    L4:
    %5 = sub nsw i32 0, 2
    store i32 %5, i32* @y, align 4
    br label %L6
    L5:
    store i32 2, i32* @y, align 4
    br label %L6
    L6:
    store i32 1, i32* @x, align 4
    br label %L3
    L2:
    store i32 0, i32* @y, align 4
    br label %L3
    L3:
    %6 = load i32, i32* @y, align 4
    %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %6)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
