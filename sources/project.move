module MyModule::CareerCounseling {
    use aptos_framework::signer;
    use aptos_framework::token;

    /// Struct representing a counseling session.
    struct Session has key, store {
        counselor: address,
        nft_required: token::TokenId,
    }

    /// Function to register a counseling session requiring a specific NFT.
    public fun register_session(owner: &signer, nft_id: token::TokenId) {
        let session = Session {
            counselor: signer::address_of(owner),
            nft_required: nft_id,
        };
        move_to(owner, session);
    }

    /// Function to book a session using the required NFT.
    public fun book_session(user: &signer, counselor: address) acquires Session {
        let session = borrow_global<Session>(counselor);
        assert!(token::exists(session.nft_required, signer::address_of(user)), 1);
        // Booking logic (e.g., sending confirmation) can be added here
    }
}
