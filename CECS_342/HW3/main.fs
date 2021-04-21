/// Card representations.
// An "enum"-type union for card suit.
type CardSuit = 
    | Spades 
    | Clubs
    | Diamonds
    | Hearts

// Kinds: 1 = Ace, 2 = Two, ..., 11 = Jack, 12 = Queen, 13 = King.
type Card = {suit : CardSuit; kind : int}


/// Game state records.
// One hand being played by the player: its cards, and a flag for whether it was doubled-down.
type PlayerHand = {
    cards: Card list; 
    doubled: bool
}

// All the hands being played by the player: the hands that are still being played (in the order the player must play them),
// and the hands that have been finished (stand or bust).
type PlayerState = {
    activeHands: PlayerHand list; 
    finishedHands: PlayerHand list
}

// The state of a single game of blackjack. Tracks the current deck, the player's hands, and the dealer's hand.
type GameState = {
    deck : Card list; 
    player : PlayerState; 
    dealer: Card list
}

// A log of results from many games of blackjack.
type GameLog = {playerWins : int; dealerWins : int; draws : int}

/// Miscellaneous enums.
// Identifies whether the player or dealer is making some action.
type HandOwner = 
    | Player 
    | Dealer

// The different actions a player can take.
type PlayerAction = 
    | Hit
    | Stand
    | DoubleDown
    | Split

// The result of one hand that was played.
type HandResult = 
    | Win
    | Lose
    | Draw


// This global value can be used as a source of random integers by writing
// "rand.Next(i)", where i is the upper bound (exclusive) of the random range.
let rand = new System.Random()


// UTILITY METHODS

// Returns a string describing a card.
let cardToString card = //Done
    // TODO: replace the following line with logic that converts the card's kind to a string.
    // Reminder: a 1 means "Ace", 11 means "Jack", 12 means "Queen", 13 means "King".
    // A "match" statement will be necessary. (The next function below is a hint.)
  
    match card.kind with
     | 1 -> sprintf "Ace of %A" card.suit
     | 2 -> sprintf "Two of %A" card.suit
     | 3 -> sprintf "Three of %A" card.suit
     | 4 -> sprintf "Four of %A" card.suit
     | 5 -> sprintf "Five of %A" card.suit
     | 6 -> sprintf "Six of %A" card.suit
     | 7 -> sprintf "Seven of %A" card.suit
     | 8 -> sprintf "Eight of %A" card.suit
     | 9 -> sprintf "Nine of %A" card.suit
     | 10 -> sprintf "Ten of %A" card.suit
     | 11 -> sprintf "Jack of %A" card.suit
     | 12 -> sprintf "Queen of %A" card.suit
     | 13 -> sprintf "King of %A" card.suit
     | _ -> sprintf "Invalid card"

    // "%A" can print any kind of object, and automatically converts a union (like CardSuit)
    // into a simple string.
    //sprintf "%d of %A" kind card.suit


// Returns a string describing the cards in a hand.    
let handToString hand = //Done

    // TODO: replace the following line with statement(s) to build a string describing the given hand.
    // The string consists of the results of cardToString when called on each Card in the hand (a Card list),
    // separated by commas. You need to build this string yourself; the built-in "toString" methods for lists
    // insert semicolons and square brackets that I do not want.
    
    List.map cardToString hand |> List.reduce(fun x y -> x + "," + y)

    // sprintf "%A" hand
    // List.fold (fun x y -> x + str + y) (List.head coll) (List.tail coll) 

    // Hint: transform each card in the hand to its cardToString representation. Then read the documentation
    // on String.concat.


    
// Returns the "value" of a card in a poker hand, where all three "face" cards are worth 10
// and an Ace has a value of 11.
let cardValue card =
    match card.kind with
    | 1 -> 11
    | 11 | 12 | 13 -> 10  // This matches 11, 12, or 13.
    | n -> n
    
    // Reminder: the result of the match will be returned


// Calculates the total point value of the given hand (Card list). 
// Find the sum of the card values of each card in the hand. If that sum
// exceeds 21, and the hand has aces, then some of those aces turn from 
// a value of 11 to a value of 1, and a new total is computed.
// TODO: fill in the marked parts of this function.
let handTotal hand = //Done
    // TODO: modify the next line to calculate the sum of the card values of each
    // card in the list. Hint: List.map and List.sum. (Or, if you're slick, List.sumBy)
    let sum = List.sumBy cardValue hand

    // TODO: modify the next line to count the number of aces in the hand.
    // Hint: List.filter and List.length. 
    let numAces = hand |> List.filter(fun card -> card.kind = 1) |> List.length
    //printfn "Num of aces: %A" numAces
    // Adjust the sum if it exceeds 21 and there are aces.
    if sum <= 21 then
        // No adjustment necessary.
        sum
    else 
        // Find the max number of aces to use as 1 point instead of 11.
        let maxAces = (float sum - 21.0) / 10.0 |> ceil |> int
        // Remove 10 points per ace, depending on how many are needed.
        sum - (10 * (min numAces maxAces))


// FUNCTIONS THAT CREATE OR UPDATE GAME STATES

// Creates a new, unshuffled deck of 52 cards.
// A function with no parameters is indicated by () in the parameter list. It is also invoked
// with () as the argument.
let makeDeck () =
    // Make a deck by calling this anonymous function 52 times, each time incrementing
    // the parameter 'i' by 1.
    // The Suit of a card is found by dividing i by 13, so the first 13 cards are Spades.
    // The Kind of a card is the modulo of (i+1) and 13. 
    List.init 52 (fun i -> let s = match i / 13 with
                                   | 0 -> Spades
                                   | 1 -> Clubs
                                   | 2 -> Diamonds
                                   | 3 -> Hearts
                           {suit = s; kind = i % 13 + 1})


// Shuffles a list by converting it to an array, doing an in-place Fisher-Yates 
// shuffle, then converting back to a list.
// Don't worry about this.
let shuffleDeck deck =
    let arr = List.toArray deck

    let swap (a: _[]) x y =
        let tmp = a.[x]
        a.[x] <- a.[y]
        a.[y] <- tmp
    
    Array.iteri (fun i _ -> swap arr i (rand.Next(i, Array.length arr))) arr
    Array.toList arr


// Creates a new game state using the given deck, dealing 2 cards to the player and dealer.
let newGame (deck : Card list) =
    // Construct the starting hands for player and dealer.
    let playerCards = [deck.Head ; List.item 2 deck] // First and third cards.
    let dealerCards = [deck.Tail.Head ; List.item 3 deck] // Second and fourth.

    // Return a fresh game state.
    {deck = List.skip 4 deck;
    // the initial player has only one active hand.
     player = {activeHands = [{cards = playerCards; doubled = false}]; finishedHands = []}
     dealer = dealerCards}


// Given a current game state and an indication of which player is "hitting", deal one
// card from the deck and add it to the given person's hand. Return the new game state.
let hit handOwner gameState = 
    let topCard = List.head gameState.deck
    let newDeck = List.tail gameState.deck
    // Updating the dealer's hand is easy.
    if handOwner = Dealer then
        let newDealerHand = topCard :: gameState.dealer
        // Return a new game state with the updated deck and dealer hand.
        {gameState with deck = newDeck;
                        dealer = newDealerHand}
    else
        // TODO: updating the player is trickier. We are always working with the player's first
        // active hand. Create a new first hand by adding the top card to that hand's card list.
        // Then update the player's active hands so that the new first hand is head of the list; and the
        //     other (unchanged) active hands follow it.
        // Then construct the new game state with the updated deck and updated player.
        
        //puts top card into activehand of player
        let playerFirstActiveHand = List.head gameState.player.activeHands

        //get player new hand after adding top card into activehand
        let newHand = {cards = topCard :: playerFirstActiveHand.cards; doubled = playerFirstActiveHand.doubled}
        //update player active hands with newHand
        let playerActiveHands = newHand :: gameState.player.activeHands
        //update gameState with player new PlayerState
        let updatedGameState = {gameState with deck = newDeck; player = {activeHands = playerActiveHands; finishedHands = gameState.player.finishedHands}}
        // {gameState with deck = newDeck;
        //                 player = {activeHands = playerActiveHands; finishedHands = gameState.player.finishedHands}//does this even work correctly?

        // }
        updatedGameState
        // printfn "New Hand = %A" newHand
        
        // TODO: this is just so the code compiles; fix it.
        // gameState


// Take the dealer's turn by repeatedly taking a single action, hit or stay, until 
// the dealer busts or stays.
let rec dealerTurn gameState =
    let dealer = gameState.dealer
    let score = handTotal dealer

    printfn "Dealer's hand: %s; %d points" (handToString dealer) score
    
    // Dealer rules: must hit if score < 17.
    if score > 21 then
        printfn "Dealer busts!"
        // The game state is unchanged because we did not hit. 
        // The dealer does not get to take another action.
        gameState
    elif score < 17 then
        printfn "Dealer hits"
        // The game state is changed; the result of "hit" is used to build the new state.
        // The dealer gets to take another action using the new state.
        gameState
        |> hit Dealer
        |> dealerTurn
    else
        // The game state is unchanged because we did not hit. 
        // The dealer does not get to take another action.
        printfn "Dealer must stay"
        gameState
        

// Take the player's turn by repeatedly taking a single action until they bust or stay.
let rec playerTurn (playerStrategy : GameState->PlayerAction) (gameState : GameState) =
    // TODO: code this method using dealerTurn as a guide. Follow the same standard
    // of printing output. This function must return the new game state after the player's
    // turn has finished, like dealerTurn.

    // Unlike the dealer, the player gets to make choices about whether they will hit or stay.
    // The "elif score < 17" code from dealerTurn is inappropriate; in its place, we will
    // allow a "strategy" to decide whether to hit. A "strategy" is a function that accepts
    // the current game state and returns true if the player should hit, and false otherwise.
    // playerTurn must call that function (the parameter playerStrategy) to decide whether
    // to hit or stay.
    let playerState = gameState.player

    if playerState.activeHands.IsEmpty then
        // A player with no active hands cannot take an action.
        gameState
    else
        // The next line is just so the code compiles. Remove it when you code the function.
        // TODO: print the player's first active hand. Call the strategy to get a PlayerAction.

        // print player's first active hand
        playerState.activeHands.Head
        
        // check strategy to get a PlayerAction
        let playerAction = playerStrategy gameState

        // Create a new game state based on that action. Recurse if the player can take another action 
        if playerAction = PlayerAction.Hit then
          printfn "Player hits"
          // The game state is changed; the result of "hit" is used to build the new state.
          // The player gets to take another action using the new state.
          let updateGame = gameState |> hit Player|> playerTurn playerStrategy
          updateGame
          
        elif playerAction = PlayerAction.Stand then
          printfn "Player stay"
          let standHand = gameState.player.activeHands.Head
          //printfn "Move active to finished: %A" (handToString standHand.cards)
          
          // let newActiveHand = List.tail gameState.player.activeHands
          let newActiveHand = []
          let finishedHand = standHand :: gameState.player.finishedHands
          //printfn "updatedFinishedHand: %A" (handToString finishedHand.Head.cards)

          let updatedGameState = {gameState with dealer = gameState.dealer; player = {activeHands = newActiveHand; finishedHands = finishedHand}}
          updatedGameState
        elif playerAction = PlayerAction.DoubleDown then
          printfn "Player doubled down"
          // hit Player once and set double down flag
          let updatedGame = gameState
                            |> hit Player 

          printfn "Player Hit"
          let playerFirstActiveHand = updatedGame.player.activeHands.Head //playerState.activeHands.Head 

          let playerNewHand = {cards = playerFirstActiveHand.cards; doubled = true}
          
          //update player active hands with newHand
          let playerActiveHands = playerNewHand :: updatedGame.player.activeHands//not being appended correctly? 
          
          //update gameState with player new PlayerState
          {gameState with player = {activeHands = playerActiveHands.Tail; finishedHands = playerActiveHands}}// {activeHands = playerActiveHands; finishedHands = gameState.player.finishedHands}

        elif playerAction = PlayerAction.Split then
          // split player hand into 2
          printfn "Player Split"
          let playerFirstActiveHand = List.head playerState.activeHands
          let firstCard = List.head playerFirstActiveHand.cards
          let secondCard = playerFirstActiveHand.cards.Tail.Head
          let newHand1 = {cards = [firstCard]; doubled = false}
          let newHand2 = {cards = [secondCard]; doubled = false}
          let playerActiveHands = newHand1 :: gameState.player.activeHands 

          // update gameState with new hands
          let update = {gameState with player = {activeHands = playerActiveHands; finishedHands = playerState.finishedHands}} 
          update
          let updateGame = update |> hit Player|> playerTurn playerStrategy
          updateGame

          let newPlayerActiveHands = newHand2 :: updateGame.player.activeHands
          //update gameState with new hands
          let newUpdate = {updateGame with player = {activeHands = newPlayerActiveHands; finishedHands = updateGame.player.finishedHands}} 
          newUpdate
          let newUpdateGame = newUpdate |> hit Player|> playerTurn playerStrategy
          newUpdateGame

          // let updateGame = {gameState with player = {activeHands = playerActiveHands; finishedHands = gameState.player.finishedHands}}
          // let nextupdate = updateGame |> hit Player 
          // // work on second split card

          // //update gameState with new hands
          // let thirdUpdate = {nextupdate with plnewPl= newPlayerActiveHands; finishedHands = nextupdate.player.finishedHands}}
          // let lastUpdate = thirdUpdate |> hit Player
          // lastUpdate
        else
          gameState
        // after their chosen one, or return the game state if they cannot.
        
        // Remove this when you're ready; it's just so the code compiles.
        // gameState
                        


// Plays one game with the given player strategy. Returns a GameLog recording the winner of the game.
let oneGame playerStrategy gameState =
    // TODO: print the first card in the dealer's hand to the screen, because the Player can see
    // one card from the dealer's hand in order to make their decisions.
    printfn "\nDealer is showing: %A" (cardToString gameState.dealer.Head) // shows dealer's first card

    printfn "Player's turn"
  
    // TODO: play the game! First the player gets their turn. The dealer then takes their turn,
    // using the state of the game after the player's turn finished.
    let playerGameTurn = playerTurn playerStrategy gameState //player plays game
    let topFinishedHand = List.head playerGameTurn.player.finishedHands
    let allFinishHand = playerGameTurn.player.finishedHands
    let allHands = playerGameTurn.player.finishedHands
    

    
    printfn "Top Finished Hands: %A" topFinishedHand
    printfn " All Finished Hands: %A" allFinishHand
    printfn "Player Score: %A" (handTotal playerGameTurn.player.finishedHands.Head.cards)
    
    printfn "\nDealer's turn"
    
    let updateGame = dealerTurn playerGameTurn //dealer plays after player
    //need to use finishedHand to count points against dealer
    let hand = updateGame.player.finishedHands
    //printfn "player finished hands %A" hand
    let Pscore = (handTotal hand.Head.cards)
    //printfn "%A" Pscore
    let Pdouble = hand.Head.doubled 
    //printfn "Double Flag: %A" Pdouble
    let Dscore = (handTotal updateGame.dealer)
    //printfn "Dealer Score: %A" Dscore
    // let logs = {playerWins = 0; dealerWins = 0; draws = 0}
 
    // TODO: determine the winner(s)! For each of the player's hands, determine if that hand is a 
    // win, loss, or draw. Accumulate (!!) the sum total of wins, losses, and draws, accounting for doubled-down
    // hands, which gets 2 wins, 2 losses, or 1 draw

    let gameLog =  {playerWins = 0; dealerWins = 0; draws = 0}
    if Pscore <= 21 && (Dscore > 21 || Pscore > Dscore) then
      printfn "Player win"
      if Pdouble = true then
        //let updatedGameLog = {gameLog with playerWins = 2}
        let updatedGameLog = {gameLog with playerWins = 2; dealerWins = 0; draws = 0}
        updatedGameLog
      else
        //let updatedGameLog = {gameLog with playerWins = 1}
        let updatedGameLog = {gameLog with playerWins = 1; dealerWins = 0; draws = 0}
        updatedGameLog
    elif Pscore <= 21 && Pscore = Dscore then
      printfn "Player draw"
      //let updatedGameLog = {gameLog with draws = 1}
      let updatedGameLog = {gameLog with playerWins = 0; dealerWins = 0; draws = 1}
      updatedGameLog
    else
      printfn "Player lose"
      if Pdouble = true then
        //let updatedGameLog = {gameLog with dealerWins = 2}
        let updatedGameLog = {gameLog with playerWins = 0; dealerWins = 2; draws = 0}
        updatedGameLog
      else
        //let updatedGameLog = {gameLog with dealerWins = 1}
        let updatedGameLog = {gameLog with playerWins = 0; dealerWins = 1; draws = 0}
        updatedGameLog

    //printfn "%A" gameLog
    //updatedGameLog
    //printfn "GameLog = %A" gameLog  //everything compiles but no updates
    // The player wins a hand if they did not bust (score <= 21) AND EITHER:
    // - the dealer busts; or
    // - player's score > dealer's score
    // If neither side busts and they have the same score, the result is a draw.

    // TODO: this is a "blank" GameLog. Return something more appropriate for each of the outcomes
    // described above.
    //logs


// Plays n games using the given playerStrategy, and returns the combined game log.
let manyGames n playerStrategy =
    // TODO: run oneGame with the playerStrategy n times, and accumulate the result. 
    // If you're slick, you won't do any recursion yourself. Instead read about List.init, 
    // and then consider List.reduce.
    //let gameState =  //makes new game 
    let initList = List.init n (fun x -> oneGame playerStrategy (makeDeck() |> shuffleDeck |> newGame)) |> List.reduce (fun acc gm -> {playerWins = acc.playerWins + gm.playerWins; dealerWins = acc.dealerWins + gm.dealerWins; draws = acc.draws + gm.draws})
    // let rec runGames n gameState playerStrategy acc = 
    //   match n with
    //   | 0 -> acc
    //   | _ -> 
    //           let playGame = oneGame playerStrategy gameState
    //           match playGame.playerWins, playGame.dealerWins, playGame.draws with
    //           | x,_,_ -> runGames (n-1) gameState playerStrategy (acc.playerWins + x)
    //           | _,y,_ -> runGames (n-1) gameState playerStrategy (acc.dealerWins + y)
    //           | _,_,z -> runGames (n-1) gameState playerStrategy (acc.draws + z)
      

    // TODO: this is a "blank" GameLog. Return something more appropriate.
    //runGames n gameState playerStrategy gameLog
    initList

        
// PLAYER STRATEGIES
// Returns a list of legal player actions given their current hand.
let legalPlayerActions playerHand =
    let legalActions = [Hit; Stand; DoubleDown; Split]
    //One boolean entry for each action; True if the corresponding action can be taken at this time.
    let requirements = [
       handTotal playerHand < 21; 
       true; 
       playerHand.Length = 2;
       playerHand.Length = 2 && cardValue playerHand.Head = cardValue playerHand.Tail.Head
    ]

    List.zip legalActions requirements // zip the actions with the boolean results of whether they're legal
    |> List.filter (fun (_, req) -> req) // if req is true, the action can be taken
    |> List.map (fun (act, _) -> act) // return the actions whose req was true


// Get a nice printable string to describe an action.
let actionToString = function
    | Hit -> "(H)it"
    | Stand -> "(S)tand"
    | DoubleDown -> "(D)ouble down"
    | Split -> "S(p)lit"

// This strategy shows a list of actions to the user and then reads their choice from the keyboard.
let rec interactivePlayerStrategy gameState =
  let playerHand = gameState.player.activeHands.Head
  let legalActions = legalPlayerActions playerHand.cards

  legalActions
  |> List.map actionToString
  |> String.concat ", "
  |> printfn "What do you want to do? %s" 

  let answer = System.Console.ReadLine()
    // Return true if they entered "y", false otherwise.
  match answer.ToLower() with
  | "h" when List.contains Hit legalActions -> Hit
  | "s" -> Stand
  | "d" when List.contains DoubleDown legalActions -> DoubleDown
  | "p" when List.contains Split legalActions -> Split
  | _ -> printfn "Please choose one of the available options, dummy."
         interactivePlayerStrategy gameState


let inactivePlayerStrategy gameState = //player can only stand 
  printfn "Player Stands"
  Stand

//Just making some notes on how to do it 

let greedyPlayerStrategy gameState = //check players hand to see if it is > 21, if not then hit
  let pHand = gameState.player.activeHands.Head.cards
  let totalHand = handTotal pHand

  if totalHand = 21 then
    printfn "BlackJack!"
    Stand
  elif totalHand > 21 then
    printfn "Bust!"
    Stand
  else
    Hit


let coinFlipPlayerStrategy gameState =
  let randNum = rand.Next(10)
  if randNum > 5 then
    Hit
  else 
    Stand
  
  
  // .nextDouble() -> 
  //take random obj, and compare 50/100 for H/T 

let basicPlayerStrategy gameState = 
  let playerHand = gameState.player.activeHands.Head.cards //gets active hand
  let dealer = gameState.dealer //get dealer hand
  let D_card1 = dealer.Head // dealer first card
  let D_card2 = dealer.Tail.Head // dealer second card
  let dealerScore = handTotal dealer //get dealer score 
  let playerScore = handTotal playerHand // get score
  let P_card1 = playerHand.Head //player card 1
  let P_card2 = playerHand.Tail.Head //player card 2
  let P_card_kind1 = P_card1.kind //get card 1 kind
  let P_card_kind2 = P_card2.kind //get card 2 kind

  match P_card_kind1, P_card_kind2 with
  | 5,5 -> DoubleDown
  | _,_ when playerScore = 11 -> DoubleDown
  | _,_ when playerScore = 10 -> if dealerScore = 10 || dealerScore = 11 then
                                      Hit
                                  else
                                    DoubleDown
  | _,_ when playerScore = 9 -> if D_card1.kind = 2 || D_card1.kind >= 7 then 
                                      Hit
                                  else
                                      DoubleDown

  | _,_ when P_card_kind1 = P_card_kind2 -> if playerScore = 20 then
                                              Stand
                                            else
                                              Split
  | _,_ when D_card1.kind >= 2 && D_card1.kind <= 6 -> if playerScore >= 12 then
                                                          Stand
                                                       else
                                                          Hit   
  | _,_ when D_card1.kind >= 7 && D_card1.kind <= 13 -> if playerScore <= 16 then
                                                          Hit
                                                        else
                                                          Stand                                           
  | _,_ when D_card1.kind = 1 -> if playerScore <= 16 && (P_card_kind1 = 1 || P_card_kind2 = 1) then
                                    Hit
                                  elif playerScore <= 11 then
                                    Hit
                                  else
                                    Stand
                                  

let testFromPDF() =
    let deck = [{suit = Hearts; kind = 5}; {suit = Clubs; kind = 13};
                {suit = Spades; kind = 5}; {suit = Clubs; kind = 13};
                {suit = Clubs; kind = 1}]
    let result = deck |> newGame |> oneGame basicPlayerStrategy
    let expected = {dealerWins = 0; playerWins = 2; draws = 0}
    assert (result = expected)


// This is a test for splitting with two 9's. The strategy should Stand on both hands after the split. One hand wins, one draws.
let splitTest() =
    let deck = [{suit = Hearts; kind = 9}; {suit = Clubs; kind = 13};
                {suit = Spades; kind = 9}; {suit = Diamonds; kind = 7};
                {suit = Clubs; kind = 1}; {suit = Clubs; kind = 8}]
    let result = deck |> newGame |> oneGame basicPlayerStrategy
    let expected = {dealerWins = 0; playerWins = 1; draws = 1}
    assert (result = expected)

    
// This test splits two 8's. One hand gets a 2 and doubles down but loses. The other hand gets an Ace, Stands, and wins.
let splitIntoDouble() =
    let deck = [{suit = Hearts; kind = 8}; {suit = Clubs; kind = 7};
                {suit = Spades; kind = 8}; {suit = Diamonds; kind = 13};
                {suit = Clubs; kind = 2}; {suit = Clubs; kind = 1}; {suit = Diamonds; kind = 2}]
    let result = deck |> newGame |> oneGame basicPlayerStrategy
    let expected = {dealerWins = 2; playerWins = 1; draws = 0}
    assert (result = expected)


[<EntryPoint>]
let main argv =

 
  //manyGames 1000 inactivePlayerStrategy |> printfn "inactivePlayerStrategy : %A" 
  //manyGames 1000 greedyPlayerStrategy |> printfn "greedyPlayerStrategy : %A" 
  manyGames 1000 coinFlipPlayerStrategy |> printfn "coinFlipPlayerStrategy : %A" 
  //manyGames 1000 basicPlayerStrategy |> printfn "basicPlayerStrategy : %A" 
  
  0
    