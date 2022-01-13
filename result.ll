@m = common global i32 0, align 4
@n = common global i32 0, align 4
@result = common global i32 0, align 4

define void @power(i32 %m, i32 %n) {
    %i = alloca i32, align 4
    store i32 1, i32* @result, align 4
    store i32 1, i32* %i, align 4
    br label %L1
    L1:
    %1 = load i32, i32* %i, align 4
    %2 = icmp sle i32 %1, %n
    br i1 %2, label %L2, label %L3
    L2:
    %3 = load i32, i32* @result, align 4
    %4 = mul nsw i32 %3, %m
    store i32 %4, i32* @result, align 4
    %5 = add nsw i32 %1, 1
    store i32 %5, i32* %i, align 4
    br label %L1
    L3:
    ret void
}

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @m)
    %2 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @n)
    %3 = load i32, i32* @m, align 4
    %4 = load i32, i32* @n, align 4
    call void @power(i32 %3, i32 %4)
    %5 = load i32, i32* @result, align 4
    %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %5)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
