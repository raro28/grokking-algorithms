export default class GCD {
    get(a, b) {
        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }

        return this.get(b, a % b);
    }
}