

class HexAI {
    constructor() {
        this.version = "1.0 Beta";
        this.author = "Hexworks";
    }

    reply(question) {
        console.log("AI is typing...");

        setTimeout(() => {
            console.log("Hello! You asked:");
            console.log(question);

            console.log("Hex AI Response:");
            console.log("This toolkit supports images, videos, models, audio and textures.");
            console.log("Enjoy using Hexworks Toolkit!");
        }, 1200);
    }
}

// Demo usage
const ai = new HexAI();
ai.reply("What does Hexworks Toolkit do?");
