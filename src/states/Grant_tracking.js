import { Machine } from 'xstate';

const grantTrackingMachine = Machine({
    id: 'grantTracking',
    initial: 'pending',
    states: {
        pending: {
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
