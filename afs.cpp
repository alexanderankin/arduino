class afs
{
public:
	static int sizeofPrint(void *a);
	static void sendCharAr(char* a);
	static void sendIntAr(int* a);
	static int* intArTest(int* a);
	
};

void setup() {
	Serial.begin(9600);
	while (!Serial) {
	}
}

void loop() {
	char a[] = {'h',
	'e',
	'l',
	'l',
	'o'};
	int b[] = {1, 2, 3, 4, 5};
	// sendCharAr(a);
	afs::sendIntAr(b);
}

int afs::sizeofPrint(void *a) {
	return (sizeof(a) * 2) + 1;
}

void afs::sendCharAr(char* a) {
	for (int i = 0; i < (sizeofPrint(a) * 2) + 1; ++i)
	{
		Serial.print(a[i]);
	}
}

void afs::sendIntAr(int* a) {
	for (int i = 0; i < sizeofPrint(a); ++i)
	{
		Serial.print(a[i]);
	}
}

int* afs::intArTest(int* a) {
	int b[afs::sizeofPrint(a)] PROGMEM;
	for (int i = 0; i < afs::sizeofPrint(a); ++i)
	{
		b[i] = a[i];
	}
	return b;
}