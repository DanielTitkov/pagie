db.createUser(
        {
            user: "pagieu",
            pwd: "pagiep",
            roles: [
                {
                    role: "readWrite",
                    db: "pagie"
                }
            ]
        }
);
