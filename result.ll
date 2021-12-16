@n = common global i32 0, align 4
@sum = common global i32 0, align 4

define i32 @main() {
    store i32 10, i32* @n, align 4
    store i32 0, i32* @sum, align 4
    br label %L1
    L1:
    %1 = load i32, i32* @n, align 4
    %2 = icmp sgt i32 %1, 0
    br i1 %2, label %L2, label %L3
    L2:
    %3 = load i32, i32* @sum, align 4
    %4 = load i32, i32* @n, align 4
    %5 = add nsw i32 %3, %4
    store i32 %5, i32* @sum, align 4
    %6 = load i32, i32* @n, align 4
    %7 = sub nsw i32 %6, 1
    store i32 %7, i32* @n, align 4
    br label %L1
    L3:
    %8 = load i32, i32* @sum, align 4
    %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %8)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
