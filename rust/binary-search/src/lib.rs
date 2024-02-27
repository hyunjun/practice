pub fn find(array: &[i32], key: i32) -> Option<usize> {
    if array.len() == 0 {
        return None;
    }
    let mut l: usize = 0;
    let mut r: usize = array.len() - 1;
    while l <= r {
        let m: usize = (l + r) / 2;
        if array[m] == key {
            return Some(m);
        }
        if array[m] < key {
            l = m + 1;
        } else {
            if m == 0 {
                return None
            }
            r = m - 1;
        }
    }
    None
}
