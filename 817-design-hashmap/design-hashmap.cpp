class MyHashMap {
public:
unordered_map<int,int>vec;
    MyHashMap() {

    }
    
    void put(int key, int value) {
        vec[key]=value;
    }
    
    int get(int key) {
        if (vec.find(key)==vec.end())return -1;
        return vec[key];
    }
    
    void remove(int key) {
        vec.erase(key);
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */