var targetSum = 24;
var currentSum = 0;
var minMove = 1;
var maxMove = 5;

function isInt(value) {
    return !isNaN(value) && 
           parseInt(Number(value)) == value && 
           !isNaN(parseInt(value, 10));
  }

function checkWinning(){
    if (currentSum < targetSum){
        return false;
    }
    else{
        return true;
    }
}

function resetGame(){
    currentSum = 0;
    document.getElementById("currentSumTxt").innerHTML = "Current Sum: " + currentSum;
    document.getElementById("computerMoveTxt").innerHTML = "";
}

function computerMove(){
    var currMod = (targetSum - currentSum) % (minMove + maxMove);
    if (currMod != 0){
        var compMove = currMod;
    }
    else{
        var compMove = Math.floor(Math.random() * (maxMove-1)) + 1;
    }
    return compMove;
    
}

function confirm()
{
    var userMoveStr = document.getElementById("userMove").value;
    if (isInt(userMoveStr) == true){
        var userMoveInt = parseInt(userMoveStr)
        if (userMoveInt > maxMove || userMoveInt < minMove){
            alert("Please enter a value between " + minMove + " and " +maxMove);
        }
        else{
            currentSum += userMoveInt;
            document.getElementById("currentSumTxt").innerHTML = "Current Sum: " + currentSum;
            if (checkWinning() == true){
                alert("You Won!");
                resetGame();
            }
            else{
                
                var compMove = computerMove();
                document.getElementById("computerMoveTxt").innerHTML = "The computer plays: " + compMove;
                currentSum += compMove;
                document.getElementById("currentSumTxt").innerHTML = "Current Sum: " + currentSum;

                if (checkWinning() == true){
                    alert("The computer Won!");
                    resetGame();
                }
            }
        }
        
    }
    else{
        alert("Please enter an integer");
    }

    
}