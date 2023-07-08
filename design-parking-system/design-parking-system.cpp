class ParkingSystem {
public:
int B=0;
int M=0;
int S=0;
    ParkingSystem(int big, int medium, int small) {
        B=big;
        M=medium;
        S=small;

    }
    
    bool addCar(int carType) {
        if (carType==1){
            B--;
            if (B>=0){
                return 1;
            }
        }
        else if (carType==2){
            M--;
            if (M>=0){
                return 1;
            }

        }
        else{
            S--;
            if (S>=0){
                return 1;
            }
        }
        return 0;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */