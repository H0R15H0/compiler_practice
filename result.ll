@m = common global i32 0, align 4
@n = common global i32 0, align 4

define i32 @power(i32 %m, i32 %n) {
    %power = alloca i32, align 4
    %1 = icmp sle i32 %n, 0
    br i1 %1, label %L1, label %L2
    L1:
    store i32 1, i32* %power, align 4
    br label %L3
    L2:
    %2 = sub nsw i32 %n, 1
    %3 = call i32 @power(i32 %m, i32 %2)
    %4 = mul nsw i32 %3, %m
    store i32 %4, i32* %power, align 4
    br label %L3
    L3:
    %5 = load i32, i32* %power, align 4
    ret i32 %5
}

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @m)
    %2 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @n)
    %3 = load i32, i32* @m, align 4
    %4 = load i32, i32* @n, align 4
    %5 = call i32 @power(i32 %3, i32 %4)
    %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %5)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
