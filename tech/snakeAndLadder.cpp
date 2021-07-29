/*
SNAKE and Ladder
-> 2 players
input 1-6

Player, Snake, Ladder
*/

class Snake{
    int head;
    int tail;
public:
    int length;

    Snake( int head, int tail)
    {
        length = head-tail;
    }

}

class Ladder{
    
    int top;
    int bottom;
public:
    int length;

    Snake( int top, int bottom)
    {
        length = top-bottom;
    }

}


class Player{
    int position;
public:
    Player()
    {
        position = 0;
    }

    int moveTo( int num)
    {
        position = position + num;

        return position;
    }

    int snakeTrap(Snake snake)
    {
        position = position - snake.length;

        return position;
    }

    int luckyLadder( Ladder ladder)
    {
        position = position - ladder.length;

        return position;
    }
}

class Board()
{
    Snake snakes[3];

    Ladder ladder[3];

    

public:
    bool finish;

    Board( ):
    {
        snakes[0] = Snake( 20, 10);
        snakes[1] = Snake( 50, 15);
        snakes[2] = Snake( 98, 30);

        ladder[0] = Ladder( 30, 20);
        ladder[1] = Ladder( 60, 25);
        ladder[2] = Ladder( 88, 40);

        finish = false;

    }

    int Dice()
    {
        //generate random number between 1-6 and return
        return num;
    }

    int Play( )
    {

    }

    int move( int num)
    
}


int main()
{
    Board(Player1 , Player2);

    return 0;
}



