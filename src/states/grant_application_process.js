import { createMachine, state, transition } from 'xstate';

const grantApplicationProcessMachine = createMachine({
    id: 'grantApplicationProcess',
    initial: 'searching',
    states: {
        searching: {
            on: {
                SELECT_GRANT: 'writing'
            }
        },
        writing: {
            on: {
                SAVE_DRAFT: 'draft',
                SUBMIT: 'submitting'
            }
        },
        draft: {
            on: {
                RESUME_WRITING: 'writing'
            }
        },
        submitting: {
            on: {
                APPROVE: 'approved',
                REJECT: 'rejected'
            }
        },
        approved: {
            type: 'final'
        },
        rejected: {
            type: 'final'
        }
    }
});
