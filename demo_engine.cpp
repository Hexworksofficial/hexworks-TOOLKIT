//(C++)

#include <iostream>
#include <string>

class HexEngine {
public:
    std::string version = "1.0 Beta";

    void start() {
        std::cout << "Hexworks Engine Started...\n";
        std::cout << "Loading Models...\n";
        std::cout << "Loading Textures...\n";
        std::cout << "Engine Ready.\n";
    }

    void aiReply(std::string msg) {
        std::cout << "AI: You said -> " << msg << "\n";
        std::cout << "AI: Hexworks Toolkit supports image, video, audio & 3D.\n";
    }
};

int main() {
    HexEngine engine;
    engine.start();
    engine.aiReply("Hello AI");

    return 0;
}
