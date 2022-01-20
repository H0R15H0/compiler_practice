@n = common global i32 0, align 4

define i32 @fact() {
    %fact = alloca i32, align 4
    %1 = load i32, i32* @n, align 4
    %2 = mul nsw i32 2, %1
    store i32 %2, i32* %fact, align 4
    %3 = load i32, i32* %fact, align 4
    ret i32 %3
}

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @n)
    %2 = call i32 @fact()
    %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %2)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
