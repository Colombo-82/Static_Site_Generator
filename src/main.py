from textnode import TextNode, TextType

def main():
    # Create a TextNode with some dummy values
    # For example, a link node with some text and a URL
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    # Print the node, which will call the __repr__ method
    print(node)

# Call the main function when the script runs
if __name__ == "__main__":
    main()