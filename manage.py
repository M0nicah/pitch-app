from app import createapp,db
from app.models import User, Pitch

# Creating app instance
app = createapp()

def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch=Pitch)

if __name__ == '__main__':
    app.run() 