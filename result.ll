@n = common global i32 0, align 4
@sum = common global i32 0, align 4
@i = common global i32 0, align 4

define i32 @main() {
    store i32 10, i32* @n, align 4
    store i32 0, i32* @sum, align 4
    store i32 1, i32* @i, align 4
    br label %L1
    L1:
    %1 = load i32, i32* @n, align 4
    %2 = load i32, i32* @i, align 4
    %3 = icmp sle i32 %2, %1
    br i1 %3, label %L2, label %L3
    L2:
    %4 = load i32, i32* @sum, align 4
    %5 = load i32, i32* @i, align 4
    %6 = add nsw i32 %4, %5
    store i32 %6, i32* @sum, align 4
    %7 = add nsw i32 %2, 1
    store i32 %7, i32* @i, align 4
    br label %L1
    L3:
    %8 = load i32, i32* @sum, align 4
    %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %8)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
