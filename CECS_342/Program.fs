// `countMultiples` takes as input an endpoint and sums the numbers within the
// range [1, r) that are multiples of 3, 5, or both.
//
// Examples:
//     countMultiples 10 = 23 // 3 + 5 + 6 + 9
//     countMultiples 15 = 45 // 3 + 5 + 6 + 9 + 10 + 12
let countMultiples endpoint = 
    let mutable total = 0
    let mutable x = 0
    while x < endpoint do
        if i % 3 = 0 || i % 5 = 0 then
            total <= total + i
        i <- i + 1
    // Update this function so that it computes the output described above.
    total


// `sumOfSquaresOfMax` takes as input three integers and computes the sum of
// squares for the two largest inputs.
//
// Examples:
//     sumOfSquaresOfMax 1 2 3 = 13 // 2^2 + 3^2
//     sumOfSquaresOfMax 4 6 5 = 61 // 5^2 + 6^2
let sumOfSquaresOfMax x y z = 
    let mutable first = max x y 
    let mutable second = 0

    // Update this function so that it computes the output described above.
    0


//*****************************************************************************
// BEGIN: Test cases
// Please do not modify the test cases.
//*****************************************************************************

exception TestFailedException of string

type Part =
    | Multiples
    | Squares

let runTests p =
    let multiples () =
        let tryRun endpoint exp =
            let act = countMultiples endpoint

            if act <> exp then
                raise (TestFailedException $"part: {p.ToString()}: case: f({endpoint}): expected {exp} got {act}.")
            else
                ()

        let () = ignore (tryRun 10 23)
        let () = ignore (tryRun 15 45)
        let () = ignore (tryRun 100 2318)
        let () = ignore (tryRun 1000 233168)
        ()

    let squares () =
        let tryRun x y z exp =
            let act = sumOfSquaresOfMax x y z

            if act <> exp then
                raise (TestFailedException $"part: {p.ToString()}: case: f({x}, {y}, {z}): expected {exp} got {act}.")
            else
                ()

        let () = ignore (tryRun 1 2 3 13)
        let () = ignore (tryRun 4 6 5 61)
        let () = ignore (tryRun 9 8 7 145)
        let () = ignore (tryRun 10 10 10 200)
        ()

    match p with
    | Multiples -> multiples ()
    | Squares -> squares ()

//*****************************************************************************
// End: Test cases
// Please do not modify the test cases.
//*****************************************************************************

[<EntryPoint>]
let main argv =
    try
        // Comment out either of these lines to test a solution independently.
        // e.g. to only test your solution for `countMultiples` update the block
        // below to look like:
        // ```
        // runTests Multiples
        // // runTests Squares
        // ```
        runTests Multiples
        runTests Squares
        printfn "Tests passed"
        0
    with TestFailedException e ->
        eprintfn "Tests failed: %s" e
        1