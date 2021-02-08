#include <stdio.h>

//	http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Database/algorithm/Quick_Sort

void quickSort(int numbers[], int array_size);
void q_sort(int numbers[], int left, int right);

void quickSort(int numbers[], int array_size)
{
	q_sort(numbers, 0, array_size -1);
}

void q_sort(int numbers[], int left, int right)
{
	int pivot, l_hold, r_hold;
	l_hold = left;
	r_hold = right;
	pivot = numbers[left]; // 0번째 원소를 피봇으로 선택
	while (left < right)
	{
		// 값이 선택한 피봇과 같거나 크다면, 이동할 필요가 없다
		while ((numbers[right] >= pivot) && (left < right))
			right --;
		// 그렇지 않고 값이 피봇보다 작다면,
		// 피봇의 위치에 현재 값을 넣는다.
		if (left != right) {
			numbers[left] = numbers[right];
		}
		// 왼쪽부터 현재 위치까지 값을 읽어들이면서
		// 피봇보다 큰 값이 있다면, 값을 이동한다.
		while ((numbers[left] <= pivot) && (left < right))
			left ++;
		if (left != right) {
			numbers[right] = numbers[left];
			right --;
		}
	}
		// 모든 스캔이 끝났다면, 피봇값을 현재 위치에 입력한다.
		// 이제 피봇을 기준으로 왼쪽에는 피봇보다 작거나 같은 값만 남았다.
		numbers[left] = pivot;
		pivot = left;
		left = l_hold;
		right = r_hold;

		// 재귀호출을 수행한다.
		if (left < pivot)
			q_sort(numbers, left, pivot - 1);
		if (right > pivot)
			q_sort(numbers, pivot+1, right);
}

int main(int argc, char **argv)
{
	//int data[] = {3,7,8,5,2,1,9,5,4};
	//int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	int data[] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
	int i;
	quickSort(data, 9);
	for (i =0; i < 9; i++)
	{
		printf("%d\n", data[i]);
	}
}
