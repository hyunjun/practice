pub fn is_leap_year(year: u64) -> bool {
    const YEAR_LEAPS: &[(u64, bool)] = &[(400, true), (100, false), (4, true)];
    for i in YEAR_LEAPS.iter() {
        if year % i.0 == 0 {
            return i.1;
        }
    }
    false
    /*
    if year % 400 == 0 {
        return true;
    }

    if year % 100 == 0 {
        return false;
    }

    if year % 4 == 0 {
        return true;
    }

    false
    */
}