#include <stdio.h>
#include <time.h>

void fizzbuzz_mod(void* str4, void* str6){
	int i;

	for(i = 1; i < 101; i++){
		if(i % 4 == 0 && i % 6 == 0)
			printf("%s%s", str4, str6);
		else if (i % 4 == 0)
			printf("%s", str4);
		else if (i % 6 == 0)
			printf("%s", str6);
		else
			printf("%d", i);
	}
}

void fizzbuzz_nomod(void* str4, void* str6){
	int i, count4, count6 = 0;

	for(i = 1; i < 101; i++){
		++count4;
		++count6;
		if(count4 != 4 && count6 != 6)
			printf("%d", i);
		if(count4 == 4){
			printf("%s", str4);
			count4 = 0;
		}
		if(count6 == 6){
			printf("%s", str6);
			count6 = 0;
		}
	}
}

int main(void){
	int i, runs;
	void* str4, * str6;
	clock_t timer_mod, timer_nomod;

	runs = 10;
	str4 = "Linked";
	str6 = "In";

   	timer_nomod = clock();
	for(i = 0; i < runs; i++)
		fizzbuzz_nomod(str4, str6);
	timer_nomod = clock() - timer_nomod;

	printf("\n");

   	timer_mod = clock();
	for(i = 0; i < runs; i++)
		fizzbuzz_mod(str4, str6);
	timer_mod = clock() - timer_mod;

    printf("\nmod took %lums\n", timer_mod);
    printf("nomod took %lums\n", timer_nomod);
	return(0);
}

