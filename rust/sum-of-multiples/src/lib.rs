//use std::collections::HashSet;

pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    /*
    let mut s = HashSet::new();
    //for num in factors {
    //    if num == &(0 as u32) {
    //        continue;
    //    }
    //    for n in 1..limit {
    //        if n % num == 0 {
    //            s.insert(n);
    //        }
    //    }
    //}
    for num in factors {
        if num == &(0 as u32) {
            continue;
        }
        s.extend((1..limit).filter(|n| n % num == 0));
    }
    s.into_iter().sum::<u32>()
     */
    //(1..limit).filter(|n| factors.iter().any(|f| &(0 as u32) < f && n % f == 0)).sum::<u32>()
    (1..limit).filter(|n| factors.iter().filter(|f| &(0 as u32) < f).any(|f| n % f == 0)).sum::<u32>()
}
