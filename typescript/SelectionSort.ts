export class SelectionSort{
    findSmallest(array: number[]): number{
        let smallest: number = array[0];
        let smallestIndex: number = 0;
        for (let i: number = 1; i < array.length; i++) {
            if(array[i] < smallest){
                smallest = array[i];
                smallestIndex = i;
            }
        }

        return smallestIndex;
    }

    sort(array: number[]): number[]{
        const result: number[] = [];
        while(array.length > 0){
            result.push(array.splice(this.findSmallest(array), 1)[0]);
        }

        return result;
    }
}