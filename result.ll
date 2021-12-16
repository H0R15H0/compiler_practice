@x = common global i32 0, align 4

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @x)
    %2 = load i32, i32* @x, align 4
    %3 = sub nsw i32 0, %2
    %4 = load i32, i32* @x, align 4
    %5 = mul nsw i32 8, %4
    %6 = sdiv i32 %5, 4
    %7 = add nsw i32 %3, %6
    %8 = sub nsw i32 %7, 1
    store i32 %8, i32* @x, align 4
    %9 = load i32, i32* @x, align 4
    %10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %9)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
