@a = common global [99 x i32] zeroinitializer, align 16
@i = common global i32 0, align 4
@n = common global i32 0, align 4

define void @initialize() {
    %i = alloca i32, align 4
    store i32 2, i32* %i, align 4
    br label %L1
    L1:
    %1 = load i32, i32* %i, align 4
    %2 = icmp sle i32 %1, 100
    br i1 %2, label %L2, label %L3
    L2:
    %3 = load i32, i32* %i, align 4
    %4 = sub nsw i32 %3, 2
    %5 = sext i32 %4 to i64
    %6 = getelementptr inbounds [99 x i32], [99 x i32]* @a, i64 0, i64 %5
    store i32 0, i32* %6, align 4
    %7 = add nsw i32 %1, 1
    store i32 %7, i32* %i, align 4
    br label %L1
    L3:
    ret void
}

define void @check(i32 %p) {
    %i = alloca i32, align 4
    store i32 %p, i32* %i, align 4
    br label %L4
    L4:
    %1 = load i32, i32* %i, align 4
    %2 = icmp sle i32 %1, 100
    br i1 %2, label %L5, label %L6
    L5:
    %3 = load i32, i32* %i, align 4
    %4 = sub nsw i32 %3, 2
    %5 = sext i32 %4 to i64
    %6 = getelementptr inbounds [99 x i32], [99 x i32]* @a, i64 0, i64 %5
    store i32 1, i32* %6, align 4
    %7 = load i32, i32* %i, align 4
    %8 = add nsw i32 %7, %p
    store i32 %8, i32* %i, align 4
    br label %L4
    L6:
    ret void
}

define i32 @main() {
    call void @initialize()
    %1 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.r, i64 0, i64 0), i32* @n)
    %2 = load i32, i32* @n, align 4
    %3 = icmp sle i32 %2, 100
    br i1 %3, label %L7, label %L8
    L7:
    store i32 2, i32* @i, align 4
    br label %L10
    L10:
    %4 = load i32, i32* @n, align 4
    %5 = load i32, i32* @i, align 4
    %6 = icmp sle i32 %5, %4
    br i1 %6, label %L11, label %L12
    L11:
    %7 = load i32, i32* @i, align 4
    %8 = sub nsw i32 %7, 2
    %9 = sext i32 %8 to i64
    %10 = getelementptr inbounds [99 x i32], [99 x i32]* @a, i64 0, i64 %9
    %11 = load i32, i32* %10, align 4
    %12 = icmp eq i32 %11, 0
    br i1 %12, label %L13, label %L14
    L13:
    %13 = load i32, i32* @i, align 4
    %14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.w, i64 0, i64 0), i32 %13)
    %15 = load i32, i32* @i, align 4
    call void @check(i32 %15)
    br label %L15
    L14:
    br label %L15
    L15:
    %16 = add nsw i32 %5, 1
    store i32 %16, i32* @i, align 4
    br label %L10
    L12:
    br label %L9
    L8:
    br label %L9
    L9:
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.w = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
declare i32 @scanf(i8*, ...)
@.str.r = private unnamed_addr constant [3 x i8] c"%d\00", align 1
