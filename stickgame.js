var targetSum = 24;
var currentSum = 0;
var minMove = 1;
var maxMove = 5;
var userTurn = true; 
// 1 is user, 2 is computer

var maxcustomTargetSum = 100
var mincustomTargetSum = 15
var maxcustomMaxMove = 10
var mincustomMaxMove = 2

function computerThinking() {
    var img = document.getElementById('thinkingImg');
    var userTurn = document.getElementById('userTurnTxt');
    img.style.visibility = 'visible';
    userTurn.style.visibility = 'hidden';
}

function ComputerNotThinking(){
    var img = document.getElementById('thinkingImg');
    var userTurn = document.getElementById('userTurnTxt');
    img.style.visibility = 'hidden';
    userTurn.style.visibility = 'visible';
}

window.onload = function() {
    ComputerNotThinking();
    randNewGame();
};



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
    document.getElementById("targetSumTxt").innerHTML = "Target Sum: " + targetSum;
    document.getElementById("mimMaxTxt").innerHTML = "Min: " + minMove + " Max: " + maxMove;
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
    computerThinking();
    setTimeout(() => { ComputerNotThinking();},1200);
    document.getElementById("computerMoveTxt").innerHTML = "The computer plays: " + compMove;
    currentSum += compMove;
    document.getElementById("currentSumTxt").innerHTML = "Current Sum: " + currentSum;

    userTurn = true;
    
    return compMove;
    
}

function confirm()
{
    if (userTurn != true){
        alert("please wait till your turn");
        return;
    }
    var userMoveStr = document.getElementById("userMove").value;
    if (isInt(userMoveStr) == true){
        var userMoveInt = parseInt(userMoveStr)
        if (userMoveInt > maxMove || userMoveInt < minMove){
            alert("Please enter a value between " + minMove + " and " +maxMove);
            return;
        }
        else{
            currentSum += userMoveInt;
            document.getElementById("currentSumTxt").innerHTML = "Current Sum: " + currentSum;
            userTurn = !userTurn;

            if (checkWinning() == true){
                alert("You Won!");
                randNewGame();
            }
            else{       
                computerMove();
                

                if (checkWinning() == true){
                    alert("The computer Won!");
                    randNewGame();
                }
            }
        }       
    }
    else{
        alert("Please enter an integer");
        return
    }
}

function newGame(){
    var newTargetSum = document.getElementById("newTarget").value;
    var newMaxMove = document.getElementById("newMax").value;
    var firstPlayer = parseInt(document.getElementById("firstPlayerDropdown").value);

    if (isInt(newTargetSum) == true){
        var newTargetSumInt = parseInt(newTargetSum);
        if (newTargetSumInt > maxcustomTargetSum || newTargetSumInt < mincustomTargetSum){
            alert("For New Target, Please enter an integer between " + mincustomTargetSum + " and " +maxcustomTargetSum);
            return;
        }
    }
    else{
        alert("For New Target, Please enter an integer between " + mincustomTargetSum + " and " +maxcustomTargetSum);
        return;
    }

    if (isInt(newMaxMove) == true){
        var newMaxMoveInt = parseInt(newMaxMove);
        if (newMaxMoveInt > maxcustomMaxMove || newMaxMoveInt < mincustomMaxMove){
            alert("For New Max Move, Please enter an integer between " + mincustomMaxMove + " and " + maxcustomMaxMove);
            return;
        }
    }
    else{
        alert("For New Max Move, Please enter an integer between " + mincustomMaxMove + " and " + maxcustomMaxMove);
        return;
    }


    if (firstPlayer == 0){
        alert("Please select a first player");
        return;
    }

    targetSum = newTargetSumInt;
    maxMove = newMaxMoveInt;
    resetGame();
    if (firstPlayer == 1){
        userTurn = True;
    }
    else{
        userTurn = false;
        computerMove();
    }
}

function randNewGame(){
    var newTargetSum = Math.floor(Math.random() * ((maxcustomTargetSum-50) - mincustomTargetSum)) + mincustomTargetSum;
    var newMaxMove = Math.floor(Math.random() * (maxcustomMaxMove - mincustomMaxMove)) + mincustomMaxMove;
    var firstPlayer = Math.floor(Math.random() * 2) + 1;


    if (isInt(newTargetSum) == true){
        var newTargetSumInt = parseInt(newTargetSum);
        if (newTargetSumInt > maxcustomTargetSum || newTargetSumInt < mincustomTargetSum){
            alert("For New Target, Please enter an integer between " + mincustomTargetSum + " and " +maxcustomTargetSum);
            return;
        }
    }
    else{
        alert("For New Target, Please enter an integer between " + mincustomTargetSum + " and " +maxcustomTargetSum);
        return;
    }

    if (isInt(newMaxMove) == true){
        var newMaxMoveInt = parseInt(newMaxMove);
        if (newMaxMoveInt > maxcustomMaxMove || newMaxMoveInt < mincustomMaxMove){
            alert("For New Max Move, Please enter an integer between " + mincustomMaxMove + " and " + maxcustomMaxMove);
            return;
        }
    }
    else{
        alert("For New Max Move, Please enter an integer between " + mincustomMaxMove + " and " + maxcustomMaxMove);
        return;
    }

    if (firstPlayer == 0){
        alert("Please select a first player");
        return;
    }

    targetSum = newTargetSumInt;
    maxMove = newMaxMoveInt;
    resetGame();
    if (firstPlayer == 1){
        userTurn = True;
    }
    
    else{
        userTurn = false;
        computerMove();
    }
    
}