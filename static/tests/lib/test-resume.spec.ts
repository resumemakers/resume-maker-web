import 'mocha'
import { expect } from 'chai'

import { Resume } from "../../src/lib/resume";

describe('Resume', () => {

    it('should initialize resume properties', () => {
        const resume = <Resume>({
            name: 'John',
            address: 'Earth'
        })

        expect(resume.name).to.equal('John')
        expect(resume.address).to.equal('Earth')
        expect(resume.profession).to.equal(undefined)
    })

    it('should be parsed to JSON', () => {
        const resume = <Resume>({ name: 'John' })
        expect('{"name":"John"}').to.equal(JSON.stringify(resume))
    })


})