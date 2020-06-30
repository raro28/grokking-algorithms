export default class GDC{
    get(a: number, b: number): number {
        if(a == 0){
            return b;
        }
        if(b == 0){
            return a;
        }

        return this.get(b, a % b);
    }
}