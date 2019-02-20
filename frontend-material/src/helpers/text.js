export function countWords(text) {
    return text.split(' ').filter(function(n) {
        return n != '';
    }).length;
}
