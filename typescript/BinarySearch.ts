export class BinarySearch {
    search(list: number[], item: number): number | null {
        let low: number = 0;
        let high: number = list.length;

        while (low <= high) {
            let mid: number = Math.floor((low + high) / 2);
            let guess: number = list[mid];

            if (guess == item) {
                return mid;
            } else if (guess > item) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return null;
    }
}