.section .rodata
.align 2

.str:
	.string "%d "
	.text
	.align 2
	.global main
.enter:
	.string "%d\n"
	.text
	.align 2
	.global main



! $r6 = i
! $r7 = j
! $r8 = cnt
! $r9 = tmp

main:
	movi	$r8, 1					! cnt = 1



! for(int i=2; i<=100; i++)

	movi	$r6, 1					! i = 2
.loop:
	slti	$r9, $r6, 100			! i < 101
	beqz 	$r9, .end
	addi	$r6, $r6, 1				! i++



! for(int j=2; j<i; j++)

	movi	$r7, 2					! j = 2
.loop2:
	slt		$r9, $r7, $r6			! j < i
	beqz	$r9, .print
	divsr	$r2, $r1, $r6, $r7		! if(i%j == 0)
	beqz	$r1, .loop
	addi	$r7, $r7, 1				! j++
	b		.loop2



.print:
	la		$r0, .str
	move	$r1, $r6
	slti	$r9, $r8, 10
	beqz	$r9, .newline
	bal		printf
	addi	$r8, $r8, 1
	b 		.loop

.newline:
	la		$r0, .enter
	bal		printf
	movi	$r8, 1
	b 		.loop



.end:
	ret
