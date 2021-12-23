@n = common global i32 0, align 4
@x = common global i32 0, align 4

define void @prime() {
    %n = alloca i32, align 4
    %1 = load i32, i32* @x, align 4
    %2 = sdiv i32 %1, 2
    store i32 %2, i32* %n, align 4
    br label %L1
    L1:
    %3 = load i32, i32* @x, align 4
    %4 = load i32, i32* @x, align 4
    %5 = load i32, i32* %n, align 4
    %6 = sdiv i32 %4, %5
    %7 = load i32, i32* %n, align 4
    %8 = mul nsw i32 %6, %7
    %9 = icmp ne i32 %3, %8
    br i1 %9, label %L2, label %L3
    L2:
    %10 = load i32, i32* %n, align 4
    %11 = sub nsw i32 %10, 1
    store i32 %11, i32* %n, align 4
    br label %L1
    L3:
    %12 = load i32, i32* %n, align 4
    %13 = icmp eq i32 %12, 1
    br i1 %13, label %L4, label %L5
    L4:
    %14 = load i32, i32* @x, align 4
    %15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %14)
    br label %L6
    L5:
    br label %L6
    L6:
    ret void
}

define i32 @main() {
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @n)
    br label %L7
    L7:
    %2 = load i32, i32* @n, align 4
    %3 = icmp slt i32 1, %2
    br i1 %3, label %L8, label %L9
    L8:
    %4 = load i32, i32* @n, align 4
    store i32 %4, i32* @x, align 4
    call void @prime()
    %5 = load i32, i32* @n, align 4
    %6 = sub nsw i32 %5, 1
    store i32 %6, i32* @n, align 4
    br label %L7
    L9:
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
