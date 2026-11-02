package io.kaarkhana.examples.s05;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import io.kaarkhana.examples.s05.DocumentAccess.Document;
import io.kaarkhana.examples.s05.DocumentAccess.User;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class DocumentAccessTest {
    private static final long OWNER = 1;
    private static final long OTHER = 2;

    /** Decision table: every combination of admin, owner and locked. */
    @ParameterizedTest(name = "admin={0} owner={1} locked={2} -> {3}")
    @CsvSource({
        "false,false,false,false",
        "false,true,false,true",
        "true,false,false,true",
        "true,true,false,true",
        "false,false,true,false",
        "false,true,true,false",
        "true,false,true,false",
        "true,true,true,false",
    })
    void everyCombinationMatchesTheRequirement(boolean admin, boolean owner, boolean locked, boolean expected) {
        var user = new User(owner ? OWNER : OTHER, admin);
        var document = new Document(OWNER, locked);
        assertEquals(expected, DocumentAccess.canEdit(user, document));
    }

    // --- Documented defect of the initial implementation (characterisation) ---

    @Test
    void initialDefectAdminCanEditALockedDocument() {
        var admin = new User(OTHER, true);
        var locked = new Document(OWNER, true);
        assertTrue(DocumentAccessInitial.canEdit(admin, locked)); // requirement says false
    }
}
